from Publisher.Dispatcher import Dispatcher
from Publisher.Publish import MessagePublisher
from Queue.QueueManager import QueueManager
from Subscriber.MessageSubcriber import MessageSubscriber


# 1. Simple Email Callback
def email_callback(messages):
    """Process email messages"""

    for message in messages:
        print(f"📧 Sending email to: {message['to']}")
        print(f"   Subject: {message['subject']}")
        # Simulate email sending
        import time
        time.sleep(0.1)  # Simulate processing time
        print(f"   ✅ Email sent successfully!")


# 2. Order Processing Callback
def order_callback(messages):
    print(messages, "Order")
    """Process order messages"""
    for message in messages:
        order_id = message['orderId']
        status = message['status']
        print(f"🛒 Processing Order #{order_id}")
        print(f"   Status: {status}")

        if status == "created":
            print(f"   → Validating order...")
        elif status == "shipped":
            print(f"   → Tracking shipment...")
        elif status == "delivered":
            print(f"   → Sending delivery confirmation...")

        print(f"   ✅ Order #{order_id} processed!")


# 3. Payment Callback with Error Handling
def payment_callback(messages):
    """Process payment messages"""
    for message in messages:
        try:
            payment_id = message['paymentId']
            amount = message['amount']
            method = message['method']

            print(f"💳 Processing Payment #{payment_id}")
            print(f"   Amount: ${amount}")
            print(f"   Method: {method}")

            # Simulate payment processing
            if amount > 1000:
                raise Exception("Payment amount too high!")

            print(f"   ✅ Payment processed successfully!")

        except Exception as e:
            print(f"   ❌ Payment failed: {e}")
            # Could implement retry logic here

# Create different types of subscribers
def create_subscribers():
    # 1. Email Service Subscriber
    email_subscriber = MessageSubscriber(
        subscriber_id="EmailService",
        callback_function=email_callback,
        batch_size=1  # Process one email at a time
    )

    # 2. Order Processing Subscriber
    order_subscriber = MessageSubscriber(
        subscriber_id="OrderProcessor",
        callback_function=order_callback,
        batch_size=3  # Process 3 orders at once
    )

    # 3. Payment Processing Subscriber
    payment_subscriber = MessageSubscriber(
        subscriber_id="PaymentProcessor",
        callback_function=payment_callback,
        batch_size=5  # Process 5 payments at once
    )

    return email_subscriber, order_subscriber, payment_subscriber


# Example usage:
def main():
    # Setup
    queue_manager = QueueManager()
    publisher = MessagePublisher(queue_manager)

    # Create queues
    queue_manager.create_queue("EmailQueue")
    queue_manager.create_queue("OrderQueue")
    queue_manager.create_queue("PaymentQueue")

    # Create subscribers
    email_sub, order_sub, payment_sub = create_subscribers()

    # Add subscribers to queues
    queue_manager.add_subscriber("EmailQueue", email_sub)
    queue_manager.add_subscriber("OrderQueue", order_sub)
    queue_manager.add_subscriber("PaymentQueue", payment_sub)

    # Publish some messages
    publisher.publish("EmailQueue", {
        "to": "customer@example.com",
        "subject": "Welcome!",
        "body": "Thanks for signing up"
    })

    publisher.publish("OrderQueue", {
        "orderId": 123,
        "status": "created",
        "customerId": 456
    })

    publisher.publish("PaymentQueue", {
        "paymentId": 789,
        "amount": 99.99,
        "method": "credit_card"
    })

    # Start consuming messages
    dispatcher = Dispatcher(queue_manager)
    dispatcher.start_consuming("EmailQueue")
    dispatcher.start_consuming("OrderQueue")
    dispatcher.start_consuming("PaymentQueue")

main()
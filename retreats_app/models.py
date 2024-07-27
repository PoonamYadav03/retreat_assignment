from django.db import models

class RetreatDetails(models.Model):
    """ 
    Retreat model with basic fields and creation.
    """
    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        help_text="Title of the retreat.",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Detailed description of the retreat.",
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=255,
        verbose_name="Location",
        help_text="Location where the retreat takes place.",
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price",
        help_text="Cost of the retreat.",
        blank=True,
        null=True,
    )
    retreat_type = models.CharField(
        max_length=50,
        verbose_name="Type",
        help_text="Type of the retreat (e.g., Signature, Standalone).",
        blank=True,
        null=True,
    )
    condition = models.CharField(
        max_length=100,
        verbose_name="Condition",
        help_text="Condition or focus area of the retreat (e.g., Mental Wellness).",
        blank=True,
        null=True,
    )
    image = models.URLField(
        verbose_name="Image",
        help_text="URL of the image representing the retreat.",
        blank=True,
        null=True,
    )
    tag = models.JSONField(
        verbose_name="Tags",
        help_text="List of tags related to the retreat.",
        blank=True,
        null=True,
    )
    duration = models.IntegerField(
        verbose_name="Duration",
        help_text="Duration of the retreat in days.",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
        help_text="Date and time when the retreat record was created.",
    )

    class Meta:
        verbose_name = "Retreat Details"
        verbose_name_plural = "Retreats Details"
        db_table = "tb_retreat"

    def __str__(self):
        return f'{self.id} {self.title}'


class BookingDetails(models.Model):
    """
    Booking model with user details, retreat reference, and creation timestamp.
    """
    user_id = models.IntegerField(
        verbose_name="User ID",
        help_text="ID of the user making the booking.",
        blank=True,
        null=True,
    )
    user_name = models.CharField(
        max_length=255,
        verbose_name="User Name",
        help_text="Name of the user making the booking.",
        blank=True,
        null=True,
    )
    user_email = models.EmailField(
        verbose_name="User Email",
        help_text="Email of the user making the booking.",
        blank=True,
        null=True,
    )
    user_phone = models.CharField(
        max_length=20,
        verbose_name="User Phone",
        help_text="Phone number of the user making the booking.",
        blank=True,
        null=True,
    )
    retreat = models.ForeignKey(
        RetreatDetails,
        on_delete=models.CASCADE,
        verbose_name="Retreat",
        help_text="Retreat that is being booked.",
        blank=True,
        null=True,
    )
    payment_details = models.JSONField(
        verbose_name="Payment Details",
        help_text="JSON data containing payment details.",
        blank=True,
        null=True,
    )
    booking_date = models.DateField(
        verbose_name="Booking Date",
        help_text="Date when the booking was made.",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date",
        help_text="Date and time when the booking record was created.",
        
    )

    class Meta:
        unique_together = ('user_id', 'retreat', 'booking_date')
        verbose_name = "Booking Details"
        verbose_name_plural = "Bookings Details"
        db_table = "tb_booking"

    def __str__(self):
        return f'{self.user_name} - {self.retreat.title}'

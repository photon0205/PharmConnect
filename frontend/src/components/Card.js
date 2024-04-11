import React, { useState } from 'react';
import './Card.css'; // Import CSS file for styling
import image from "../i2.png"
const Card = ({ product }) => {
  const [quantity, setQuantity] = useState(1);

  const handleIncrement = () => {
    setQuantity(quantity + 1);
  };

  const handleDecrement = () => {
    if (quantity > 1) {
      setQuantity(quantity - 1);
    }
  };

  const handleBuyNow = () => {
    // You can navigate to the checkout page or perform any other action here
    console.log(`Buying ${quantity} ${product.name}`);
  };

  return (
    <div className="card">
      <div className="image-container">
        <img src={image} alt={"DETTOL"} className="product-image" />
      </div>
      <div className="product-details">
        <h2>DETTOL</h2>
        <p>Kharido bhai</p>
        <div className="quantity-controls">
          <button onClick={handleDecrement}>-</button>
          <input type="text" value={quantity} readOnly />
          <button onClick={handleIncrement}>+</button>
        </div>
        <button className="buy-now-button" onClick={handleBuyNow}>Buy Now</button>
      </div>
    </div>
  );
};

export default Card;

import { Component, input, output } from '@angular/core';
import { Product } from '../../models/product.model';
@Component({
  selector: 'app-product-item',
  standalone: true,
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {

  product = input.required<Product>();
  delete = output<number>();

  like() {
    this.product().likes++;
  }

  
  
share() {
  window.open(`https://wa.me/?text=${this.product().link}`);
}
  
  openKaspi() {
  window.open(this.product().link, '_blank');
}
//
   remove() {
  if (this.product().likes >= 10) {
    alert('Товар не может быть удален');
    return;
  }

  if (confirm('Удалить товар?')) {
    this.delete.emit(this.product().id);
  }
}
}
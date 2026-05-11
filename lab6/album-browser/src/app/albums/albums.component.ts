import { Component, OnInit } from '@angular/core';
import { AlbumService } from '../services/album.service';
import { Album } from '../models/album.model';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css'] 
})

export class AlbumsComponent implements OnInit {

  albums: Album[] = [];
  loading = true;

  constructor(private albumService: AlbumService) {}
  newTitle = '';

  ngOnInit(): void {
  this.loading = true;

  this.albumService.getAlbums().subscribe({
    next: (data) => {
      this.albums = data;
      this.loading = false;
    },
    error: (err) => {
      console.error(err);
      this.loading = false;
    }
  });
}

loadAlbums() {
  this.loading = true;

  this.albumService.getAlbums().subscribe(data => {
    this.albums = data;
    this.loading = false;
  });
}

  delete(id: number) {
    this.albumService.deleteAlbum(id).subscribe(() => {
      this.albums = this.albums.filter(a => a.id !== id);
    });
  }
  create() {
  const newAlbum: Album = {
    userId: 1,
    id: 0,
    title: this.newTitle
  };

  this.albumService.createAlbum(newAlbum).subscribe(res => {
    this.albums.unshift(res);
    this.newTitle = '';
  });
}
sortAsc() {
  this.albums = [...this.albums].sort((a, b) =>
    a.title.localeCompare(b.title, undefined, { sensitivity: 'base' })
  );
}

sortDesc() {
  this.albums = [...this.albums].sort((a, b) =>
    b.title.localeCompare(a.title, undefined, { sensitivity: 'base' })
  );
}
}
import {Component, signal} from '@angular/core';

@Component({
  selector: 'app-form-login',
  imports: [],
  templateUrl: './form-login.component.html',
  styleUrl: './form-login.component.css'
})

export class FormLoginComponent {
  titre= signal('Formulaire de connexion')
  hide = signal(true)
  valueInputUsername = signal('Ilyes')
  clickLogin(): void{
    this.hide.update((val) => {return !val;} )
    console.log('test', this.hide())
  }
}

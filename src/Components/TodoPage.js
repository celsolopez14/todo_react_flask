import React,{useState, useEffect} from 'react'
import { Card } from './Card'

export const TodoPage = ()=>{

    const[todo, setTodo] = useState([])

    useEffect(() =>{
        fetch('/api').then(response =>{
            if(response.ok){
                return response.json()
            }
        }).then(data => setTodo(data) )
    }, [])
    return (
        <Card  listTodos={todo}/>
    )
}
  



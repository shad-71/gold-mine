//***********************************************************************************
//  LinkedList.cpp
//
//  Created by Shadab on March 31, 2017.
//  This source file contains the LinkedList implementation.
//***********************************************************************************

#include "LinkedList.h"

// Default Constructor creates the head node.
LinkedList::LinkedList()
{
    cout << "\nEntering Constructor ..." << endl;
    head = new node;
    head -> song = "head (contains no song data)";
    head -> artist = "head (contains no artist data)";
    head -> next = NULL;
    listLength = 0;
    cout << "Success: head node created. listLength set to 0." << endl;
}

// Setter adds a node to the list at a given position.
// Takes a node and list position as parameters.
// Position must be between 1 and the number of data nodes.
// Returns true if the operation is successful.
bool LinkedList::insertNode( node * newNode, int position )
{
    cout << "\nEntering insertNode ..." << endl;
    if ( (position <= 0) || (position > listLength + 1) )
    {
        cout << "Error: the given position is out of range." << endl;
        return false;
    }
    if (!head -> next)
    {
        head -> next = newNode;
        listLength++;
        cout << "Success: added '" << newNode -> song << "' to position " << position << ".\n";
        cout << "listLength = " << listLength << endl;
        return true;
    }
    int count = 0;
    node * p = head;
    node * q = head;
    while (q)
    {
        if (count == position)
        {
            p -> next = newNode;
            newNode -> next = q;
            listLength++;
            cout << "Success: added '" << newNode -> song << "' to position " << position << ".\n";
            cout << "listLength = " << listLength << endl;
            return true;
        }
        p = q;
        q = p -> next;
        count++;
    }
    if (count == position)
    {
        p -> next = newNode;
        newNode -> next = q;
        listLength++;
        cout << "Success: added '" << newNode -> song << "' to position " << position << ".\n";
        cout << "listLength = " << listLength << endl;
        return true;
    }
    cout << "Error: song node was not added to list." << endl;
    return false;
}

// Setter removes a node by its given position.
// Returns true if the operation is successful.
bool LinkedList::removeNode( int position )
{
    cout << "\nEntering removeNode..." << endl;
    if ( (position <= 0) || (position > listLength + 1) )
    {
        cout << "Error: the given position is out of range." << endl;
        return false;
    }
    if (!head -> next)
    {
        cout << "Error: there is nothing to remove." << endl;
        return false;
    }
    
    int count = 0;
    node * p = head;
    node * q = head;
    while (q)
    {
        if (count == position)
        {
            p -> next = q -> next;
            delete q;
            listLength--;
            cout << "Success: node at position " << position << " was deleted." << endl;
            cout << "listLength = " << listLength << endl;
            return true;
        }
        p = q;
        q = p -> next;
        count++;
    }
    cout << "Error: nothing was removed from the list." << endl;
    return false;
}

// Prints each node in the list in consecutive order,
// starting at the head and ending at the tail.
// Prints list data to the console.
void LinkedList::printList()
{
    cout << "\nEntered printList..." << endl;
    int count = 0;
    node * p = head;
    node * q = head;
    cout << "\n---------------------\n";
    cout << " Song Playlist\n";
    while (q)
    {
        p = q;
        cout << "---------------------\n";
        cout << "\t position: " << count << "\n";
        cout << "\t song: " << p -> song << "\n";
        cout << "\t artist: " << p -> artist << "\n";
        q = p -> next;
        count++;
    }
}

 //Insert new node at the beginning of LinkedList
 bool LinkedList::push( node * newNode)
 {
     newNode -> next = head;
     head = newNode;
     listLength++;
     cout << "New Item pushed \n";
     return true;

 }


// Destructor de-allocates memory used by the list.
LinkedList::~LinkedList()
{
    cout << "\nEntering Destructor..." << endl;
    node * p = head;
    node * q = head;
    while (q)
    {
        p = q;
        q = p -> next;
        delete p;
    }
    cout << "Success: list is deleted." << endl;
}